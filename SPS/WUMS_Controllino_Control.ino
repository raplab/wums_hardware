#include <SPI.h>
#include <Controllino.h>
#include <Ethernet.h>

//get request must follow the following structure
//http://172.31.19.153/WRITEPI?ADR1=D01&VALUE1=0&FORMAT1=%25d
//this is due to a system legacy problem and we emulate the request structure that a wago sps uses
//ADR1 = D00-D.. - change the range according to the controllino digital outs and match it with the system
//VALUE1 = 0 > ADR1 OFF
//VALUE1 = 1 > ADR1 ON

String request = "";

//set your own mac address and make sure that its unique
byte mac[] = {
  0x50, 0xD7, 0x53, 0x00, 0x04, 0x4A
};

//initialize the server on port 80
EthernetServer server(80);

void setup() {

  Serial.begin(9600);
  //init ethernet 
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    for(;;)
      ;
  }
  // print your local IP address:
  Serial.print("Server up and running: ");
  Serial.println(Ethernet.localIP());
 
  //define all the outputs -> adjust this to the type of controllino that u use
  pinMode(CONTROLLINO_D0, OUTPUT); 
  pinMode(CONTROLLINO_D1, OUTPUT);
  pinMode(CONTROLLINO_D2, OUTPUT);
  pinMode(CONTROLLINO_D3, OUTPUT);
  pinMode(CONTROLLINO_D4, OUTPUT);
  pinMode(CONTROLLINO_D5, OUTPUT);
  pinMode(CONTROLLINO_D6, OUTPUT);
  pinMode(CONTROLLINO_D7, OUTPUT);

  delay(100);
  //run the server
  server.begin();
}

void loop() {

  EthernetClient client = server.available();

  if (client) {

    while (client.connected()) {
      if (client.available()) {

        boolean currentLineIsBlank = true;
        char c = client.read();
        request += c;

        if (c == '\n' && currentLineIsBlank) {
          //parse the request to get the pin and highorlow state
          String subrequest = request.substring(request.indexOf('A'), request.indexOf('%'));
          String addr = split(subrequest, '&', 0); 
          String state = split(subrequest, '&', 1); 
          String highorlow = state.substring(state.length() - 1);
          String outlet = addr.substring(addr.length() - 2); 

          client.flush();
          //turn specific pin on or off
          if (outlet.charAt(0) == 'D') {
            String outletshort = String(outlet.charAt(1));
            if(outletshort == '0') {
              toggle(0, highorlow.toInt());
            }else{
               toggle(outletshort.toInt(), highorlow.toInt());
            }
          } else {
            toggle(outlet.toInt(), highorlow.toInt());
          }

          //return a valid HTTP OK
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");
          client.print("<h1>You turned the knobs and something happend!</h1>");
          client.println("</html>");

          delay(100);
          //stop the connection
          client.stop();
          break;
        }
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
        } else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }

      }
    }
  }
  request = "";
  // give the web browser time to receive the data
  delay(100);
  // close the connection:
  client.stop();
}

void toggle(int id, int onoff){
  //turns specific pins (id) on or off (onoff)
  //adjust this to match the pins of your controllino
  switch(id){
    case 0:
      digitalWrite(CONTROLLINO_D0,onoff);
      break;

    case 1:
      digitalWrite(CONTROLLINO_D1,onoff);
      break;

    case 2:
      digitalWrite(CONTROLLINO_D2,onoff);
      break;

    case 3:
      digitalWrite(CONTROLLINO_D3,onoff);
      break;

    case 4:
      digitalWrite(CONTROLLINO_D4,onoff);
      break;

    case 5:
      digitalWrite(CONTROLLINO_D5,onoff);
      break;

    case 6:
      digitalWrite(CONTROLLINO_D6,onoff);
      break;

    case 7:
      digitalWrite(CONTROLLINO_D7,onoff);
      break;

    default:
      break;
  }
}

String split(String s, char parser, int index) {
  //split a string according to a parser and return a certain index
  String rs = "";
  int parserIndex = index;
  int parserCnt = 0;
  int rFromIndex = 0, rToIndex = -1;
  while (index >= parserCnt) {
    rFromIndex = rToIndex + 1;
    rToIndex = s.indexOf(parser, rFromIndex);
    if (index == parserCnt) {
      if (rToIndex == 0 || rToIndex == -1) return "";
      return s.substring(rFromIndex, rToIndex);
    } else parserCnt++;
  }
  return rs;
}
