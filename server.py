import grpc
from concurrent import futures
import time


import calculator_pb2
import calculator_pb2_grpc

import calculator


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):


    def Add(self, request, context):
        response = calculator_pb2.Response()
        response.result = calculator.add(request.n1,request.n2)
        print ('Result:',response.result)
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()


try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)