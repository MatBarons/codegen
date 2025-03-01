import { ActionReducerMap } from '@ngrx/store';
import { LoaderState } from '../../core/loader/loader-state/reducers/loader.reducer';
import { LoaderReducers } from '../../core/loader/loader-state/reducers';
import { AuthState } from '../../core/user/auth-state/reducers/auth.reducers';
import { AuthReducers } from '../../core/user/auth-state/reducers';
import { SnackbarState } from '../../core/snackbars/snackbars-state/reducers/snackbars.reducers';
import { SnackbarsReducers } from '../../core/snackbars/snackbars-state/reducers';
import { routerReducer, RouterReducerState } from '@ngrx/router-store';

export interface AppState {
  loaderState: LoaderState;
  snackbarState: SnackbarState;
  userState: AuthState;
  router: RouterReducerState;
}

export const appReducer: ActionReducerMap<AppState> = {
  loaderState: LoaderReducers.loaderReducer,
  snackbarState: SnackbarsReducers.snackbarsReducer,
  userState: AuthReducers.userReducer,
  router: routerReducer,
};
