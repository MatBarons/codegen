import { User } from '../../user.model';
import { Action, createReducer, on } from '@ngrx/store';
import { AuthActions } from '../actions';

export interface AuthState {
  user: User | null;
}

const initialState: AuthState = {
  user: null
};
const reducer = createReducer(
  initialState,
  on(
    AuthActions.storeUser,
    (state, action): AuthState => ({ ...state, user: action })
  ),
  on(AuthActions.clearUser, (state): AuthState => ({ ...state, user: null })),
);

export function userReducer(
  state: AuthState | undefined,
  action: Action
): AuthState {
  return reducer(state, action);
}
