import { createSelector } from '@ngrx/store'
import { selectAppState } from '../../../../app-state/app-selectors/app.selectors'
import { AppState } from '../../../../app-state/app-reducers/app.reducers'
import { SnackbarState } from '../reducers/snackbars.reducers'
import { Snackbar } from '../../snackbars.model'


export const selectSnackbarState = createSelector(
  selectAppState,
  (s: AppState): SnackbarState => s.snackbarState
)
export const selectSnackbar = createSelector(
  selectSnackbarState,
  (s: SnackbarState): Snackbar | null => s.snackbar
)
