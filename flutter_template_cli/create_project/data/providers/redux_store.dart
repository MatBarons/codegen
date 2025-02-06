import 'package:redux/redux.dart';


// Singleton Manager for Multiple Stores
class ReduxStoreManager {
  static final ReduxStoreManager _instance = ReduxStoreManager._internal();

  // Private constructor
  ReduxStoreManager._internal();

  // Public factory constructor
  factory ReduxStoreManager() {
    return _instance;
  }

  // Map to hold stores of different types
  final Map<Type, dynamic> _stores = {};

  void init<T>(Store<T> store) {
    // Check if the store type is already initialized
    if (!_stores.containsKey(T)) {
      _stores[T] = store;
    }
  }

  Store<T> getStore<T>() {
    if (!_stores.containsKey(T)) {
      throw Exception("Store of type $T is not initialized");
    }
    return _stores[T];
  }
}