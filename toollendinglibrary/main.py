
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)

  if request.find('D0') != -1:
    tool_00.value(0)
    sleep(0.5)
    tool_00.value(1)

  elif request.find('D1') != -1:
    tool_01.value(0)
    sleep(0.5)
    tool_01.value(1)

  elif request.find('D2') != -1:
    tool_02.value(0)
    sleep(0.5)
    tool_02.value(1)

  elif request.find('D3') != -1:
    tool_03.value(0)
    sleep(0.5)
    tool_03.value(1)

  elif request.find('D4') != -1:
    tool_04.value(0)
    sleep(0.5)
    tool_04.value(1)

  elif request.find('D5') != -1:
    tool_05.value(0)
    sleep(0.5)
    tool_05.value(1)

  elif request.find('D6') != -1:
    tool_06.value(0)
    sleep(0.5)
    tool_06.value(1)

  elif request.find('D7') != -1:
    tool_07.value(0)
    sleep(0.5)
    tool_07.value(1)

  elif request.find('D8') != -1:
    tool_08.value(0)
    sleep(0.5)
    tool_08.value(1)

  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.send('<!DOCTYPE HTML>\n');
  conn.send('<html>\n');
  conn.send('<h1>You turned the knobs and something happened!</h1>\n');
  conn.send('</html>\n');
  conn.close()
