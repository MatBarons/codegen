class ErrorState {
  final bool isErrorVisible;
  final int statusCode;

  ErrorState({
    required this.isErrorVisible,
    this.statusCode = 0,
  });

  ErrorState copyWith({
    required bool isErrorVisible,
    int? statusCode,
  }) {
    return ErrorState(
      isErrorVisible: isErrorVisible,
      statusCode: statusCode ?? this.statusCode,
    );
  }
}
