import '../error_state/error_state.dart';
import '../loader_state/loader_state.dart';

class AppState {
  final ErrorState errorState;
  final LoaderState loaderState;

  AppState({
    required this.errorState,
    required this.loaderState
  });

  AppState copyWith({
    ErrorState? errorState,
    LoaderState? loaderState
  }) {
    return AppState(
      errorState: errorState ?? this.errorState,
      loaderState: loaderState ?? this.loaderState
    );
  }

  factory AppState.initial() {
    return AppState(
      errorState: ErrorState(isErrorVisible: false),
      loaderState: LoaderState(loaders: 0)
    );
  }
}
