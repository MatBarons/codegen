import 'package:redux/redux.dart';
import '../loader_state.dart';

import '../actions/loader_actions.dart';

final loaderReducer = combineReducers<LoaderState>([
  TypedReducer<LoaderState,OpenLoader>(_onOpen),
  TypedReducer<LoaderState,CloseLoader>(_onClose)
]);

LoaderState _onOpen(LoaderState state,OpenLoader action) => state.copyWith(loaders: state.loaders +1);

LoaderState _onClose(LoaderState state,CloseLoader action) => state.copyWith(loaders: state.loaders -1);