import 'package:flutter/material.dart';
import 'package:flutter_redux/flutter_redux.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import '../providers/app_state/app_state.dart';
import '../providers/error_state/actions/error_actions.dart';
import '../providers/error_state/error_state.dart';
import '../providers/redux_store.dart';

class ErrorDialog extends StatefulWidget {
  const ErrorDialog({super.key});

  @override
  State<ErrorDialog> createState() => _ErrorDialogState();
}

class _ErrorDialogState extends State<ErrorDialog> {

  @override
  Widget build(BuildContext context) {
    return StoreProvider<AppState>(
      store: ReduxStoreManager().getStore<AppState>(),
      child: StoreConnector<AppState,ErrorState>(
        builder: (context, vm){
          if (vm.isErrorVisible) {
            WidgetsBinding.instance.addPostFrameCallback((_) {
              showDialog(context: context, builder: (_) => AlertDialog(
                title: Text(AppLocalizations.of(context)!.http_error_title),
                content: Text(AppLocalizations.of(context)!.http_error_message + vm.statusCode.toString()),
              )).then((_) => {
                ReduxStoreManager().getStore<AppState>().dispatch(HideError())
              });
            });
          }
          return const SizedBox(height: 28);
        },
        converter: (store) => store.state.errorState)
    );

  }
}