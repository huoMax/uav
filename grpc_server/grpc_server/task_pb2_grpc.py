# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from grpc_server import task_pb2 as grpc__server_dot_task__pb2


class TaskServiceStub(object):
    """python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. task.proto

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.task_face_recognition = channel.unary_unary(
                '/TaskService/task_face_recognition',
                request_serializer=grpc__server_dot_task__pb2.FaceRecognitionRequest.SerializeToString,
                response_deserializer=grpc__server_dot_task__pb2.FaceRecognitionReplay.FromString,
                )
        self.heartbeat = channel.unary_unary(
                '/TaskService/heartbeat',
                request_serializer=grpc__server_dot_task__pb2.HeartbeatRequest.SerializeToString,
                response_deserializer=grpc__server_dot_task__pb2.HeartbeatReplay.FromString,
                )
        self.test = channel.unary_unary(
                '/TaskService/test',
                request_serializer=grpc__server_dot_task__pb2.HeartbeatRequest.SerializeToString,
                response_deserializer=grpc__server_dot_task__pb2.HeartbeatReplay.FromString,
                )


class TaskServiceServicer(object):
    """python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. task.proto

    """

    def task_face_recognition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def heartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def test(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'task_face_recognition': grpc.unary_unary_rpc_method_handler(
                    servicer.task_face_recognition,
                    request_deserializer=grpc__server_dot_task__pb2.FaceRecognitionRequest.FromString,
                    response_serializer=grpc__server_dot_task__pb2.FaceRecognitionReplay.SerializeToString,
            ),
            'heartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.heartbeat,
                    request_deserializer=grpc__server_dot_task__pb2.HeartbeatRequest.FromString,
                    response_serializer=grpc__server_dot_task__pb2.HeartbeatReplay.SerializeToString,
            ),
            'test': grpc.unary_unary_rpc_method_handler(
                    servicer.test,
                    request_deserializer=grpc__server_dot_task__pb2.HeartbeatRequest.FromString,
                    response_serializer=grpc__server_dot_task__pb2.HeartbeatReplay.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TaskService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TaskService(object):
    """python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. task.proto

    """

    @staticmethod
    def task_face_recognition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskService/task_face_recognition',
            grpc__server_dot_task__pb2.FaceRecognitionRequest.SerializeToString,
            grpc__server_dot_task__pb2.FaceRecognitionReplay.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def heartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskService/heartbeat',
            grpc__server_dot_task__pb2.HeartbeatRequest.SerializeToString,
            grpc__server_dot_task__pb2.HeartbeatReplay.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def test(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskService/test',
            grpc__server_dot_task__pb2.HeartbeatRequest.SerializeToString,
            grpc__server_dot_task__pb2.HeartbeatReplay.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
