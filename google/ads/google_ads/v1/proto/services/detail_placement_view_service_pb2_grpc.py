# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import detail_placement_view_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_detail__placement__view__pb2
from google.ads.google_ads.v1.proto.services import detail_placement_view_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_detail__placement__view__service__pb2


class DetailPlacementViewServiceStub(object):
  """Proto file describing the Detail Placement View service.

  Service to fetch Detail Placement views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetDetailPlacementView = channel.unary_unary(
        '/google.ads.googleads.v1.services.DetailPlacementViewService/GetDetailPlacementView',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_detail__placement__view__service__pb2.GetDetailPlacementViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_detail__placement__view__pb2.DetailPlacementView.FromString,
        )


class DetailPlacementViewServiceServicer(object):
  """Proto file describing the Detail Placement View service.

  Service to fetch Detail Placement views.
  """

  def GetDetailPlacementView(self, request, context):
    """Returns the requested Detail Placement view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DetailPlacementViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetDetailPlacementView': grpc.unary_unary_rpc_method_handler(
          servicer.GetDetailPlacementView,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_detail__placement__view__service__pb2.GetDetailPlacementViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_detail__placement__view__pb2.DetailPlacementView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.DetailPlacementViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))