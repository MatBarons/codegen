import 'package:flutter/material.dart';
import 'package:flutter_redux/flutter_redux.dart';

import '../providers/app_state/app_state.dart';
import '../providers/redux_store.dart';

class DisplayLoader{
  OverlayEntry? _overlay;

  DisplayLoader();

  void show(BuildContext context) {
    if(_overlay == null){
      _overlay = OverlayEntry(
        // replace with your own layout
        builder: (context) => const ColoredBox(
          color: Color(0x80000000),
          child: Center(
            child: CircularProgressIndicator(
              valueColor: AlwaysStoppedAnimation(Colors.white),
            ),
          ),
        ),
      );
      Overlay.of(context).insert(_overlay!);
    }

  }

  void hide() {
    if(_overlay != null){
      _overlay!.remove();
      _overlay = null;
    }
  }
}

class Loader extends StatelessWidget {
  final DisplayLoader _loader = DisplayLoader();
  Loader({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: StoreProvider(
          store: ReduxStoreManager().getStore<AppState>(),
          child: StoreConnector<AppState,int>(
              converter: (store) => store.state.loaderState.loaders,
              distinct: true,
              builder: (context, vm) {
                if(vm != 0){
                  WidgetsBinding.instance.addPostFrameCallback((_) {
                    _loader.show(context);
                  });
                }else{
                  _loader.hide();
                }
                return const SizedBox(
                  height: 16,
                );
              })),
    );
  }
}