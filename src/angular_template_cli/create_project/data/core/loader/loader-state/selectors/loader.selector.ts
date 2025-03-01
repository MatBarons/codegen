import { createSelector } from '@ngrx/store'
import { selectAppState } from '../../../../app-state/app-selectors/app.selectors'
import { AppState } from '../../../../app-state/app-reducers/app.reducers'
import { LoaderState } from '../reducers/loader.reducer'

export const selectLoaderState = createSelector(
  selectAppState,
  (a: AppState): LoaderState => a.loaderState
)
export const selectLoadersState = createSelector(
  selectLoaderState,
  (a: LoaderState): number => a.loaders
)
