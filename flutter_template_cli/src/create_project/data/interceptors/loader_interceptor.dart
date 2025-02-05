import 'dart:async';
import '../../providers/app_state/app_state.dart';
import '../../providers/loader_state/actions/loader_actions.dart';
import '../../providers/redux_store.dart';
import 'package:http/http.dart';
import 'package:http_interceptor/models/interceptor_contract.dart';


class LoaderInterceptor implements InterceptorContract {

  @override
  Future<BaseRequest> interceptRequest({required BaseRequest request}) async {
    ReduxStoreManager().getStore<AppState>().dispatch(OpenLoader());
    return request;
  }

  @override
  Future<BaseResponse> interceptResponse({required BaseResponse response}) async {
    ReduxStoreManager().getStore<AppState>().dispatch(CloseLoader());
    return response;
  }

  @override
  Future<bool> shouldInterceptRequest() async {
    return true;
  }

  @override
  Future<bool> shouldInterceptResponse() async {
    return true;
  }

}
