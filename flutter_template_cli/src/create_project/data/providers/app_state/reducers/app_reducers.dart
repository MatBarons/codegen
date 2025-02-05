import '../../error_state/reducers/error_reducers.dart';
import '../../loader_state/reducers/loader_reducers.dart';
import '../app_state.dart';


AppState appReducer(AppState state, dynamic action) {
  return AppState(
    errorState: errorReducer(state.errorState, action),
    loaderState: loaderReducer(state.loaderState, action)
  );
}