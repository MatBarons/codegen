import '../actions/error_actions.dart';
import '../error_state.dart';
import 'package:redux/redux.dart';


final errorReducer = combineReducers<ErrorState>([
  TypedReducer<ErrorState,ShowError>(_onShow),
  TypedReducer<ErrorState,HideError>(_onHide)
]);

ErrorState _onShow(ErrorState state,ShowError action) => state.copyWith(isErrorVisible: true,statusCode: action.statusCode);

ErrorState _onHide(ErrorState state,HideError action) => state.copyWith(isErrorVisible: false);