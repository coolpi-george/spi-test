import spidev

spi = spidev.SpiDev()
spi.open(1, 0)
spi.max_speed_hz = 24000000
spi.mode = 3

while True:
    input_str = input("Please enter multiple hexadecimal numbers separated by spaces, or 'exit' to quit：")
    if input_str == 'exit':
        break
    hex_numbers = input_str.split()
    data = [int(num, 16) for num in hex_numbers]
    print("The input hexadecimal value：", data)
    response = spi.xfer(data)
    print("Received:", response)

spi.close()
