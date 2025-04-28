import 'dart:async';
import '../../providers/app_state/app_state.dart';
import '../../providers/error_state/actions/error_actions.dart';
import '../../providers/redux_store.dart';
import 'package:http/http.dart';
import 'package:http_interceptor/models/interceptor_contract.dart';


class ErrorInterceptor implements InterceptorContract {

  @override
  Future<BaseRequest> interceptRequest({required BaseRequest request}) async {
    return request;
  }

  @override
  Future<BaseResponse> interceptResponse(
      {required BaseResponse response}) async {
    if(response.statusCode >= 400){
      ReduxStoreManager().getStore<AppState>().dispatch(
          ShowError(response.statusCode)
      );
    }
    return response;
  }

  @override
  Future<bool> shouldInterceptRequest() async {
    return false;
  }

  @override
  Future<bool> shouldInterceptResponse() async {
    return true;
  }

}
