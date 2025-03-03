class LoaderState {
  final int loaders;

  LoaderState({
    required this.loaders,
  });

  LoaderState copyWith({
    required int loaders
  }) {
    return LoaderState(
      loaders: loaders,
    );
  }
}