import grpc
from concurrent import futures
import image_pb2
import image_pb2_grpc
from extraction import Extraction
class UploadFileServicer(image_pb2_grpc.UploadFileServicer):
    def uploadFile(self, request, context):
        # Implement file upload logic here
        print("Received request:")
        print("Path: ", request.path)
        print("Object ID: ", request.objectId)
        return image_pb2.FileUploadRes(status="success")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_UploadFileServicer_to_server(UploadFileServicer(), server)
    server.add_insecure_port('[::]:23010')
    server.start()
    print("Server started on port 23010")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()