import { createSelector } from '@ngrx/store';
import { selectAppState } from '../../../../app-state/app-selectors/app.selectors';
import { AppState } from '../../../../app-state/app-reducers/app.reducers';
import { AuthState } from '../reducers/auth.reducers';
import { User } from '../../user.model';

export const selectUserState = createSelector(
  selectAppState,
  (s: AppState): AuthState => s.userState
);

export const selectUser = createSelector(
  selectUserState,
  (s: AuthState): User | null => s.user
);
