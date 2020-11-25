import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')


s = calculator_pb2_grpc.CalculatorStub(channel)

# create request message
numbers = calculator_pb2.Request(n1=int(input("Enter number1: ")),n2=int(input("Enter number2: ")))

response = s.Add(numbers)
