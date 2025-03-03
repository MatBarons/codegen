
import { Action, createReducer, on } from '@ngrx/store'
import { Snackbar } from '../../snackbars.model'
import { SnackbarsActions } from '../actions'


export interface SnackbarState {
  snackbar: Snackbar | null
}

const initialState: SnackbarState = {
  snackbar: null
}

const reducer = createReducer(
  initialState,
  on(SnackbarsActions.storeSnackbar, (state, action): SnackbarState => ({ ...state, snackbar: action.s})),
  on(SnackbarsActions.clearSnackbar, (state): SnackbarState => ({ ...state, snackbar: null }))
)

export function snackbarsReducer (state: SnackbarState | undefined, action: Action): SnackbarState {
  return reducer(state, action)
}
