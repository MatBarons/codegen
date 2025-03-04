import { createAction, props } from '@ngrx/store'
import { Snackbar } from '../../snackbars.model'


export const storeSnackbar = createAction('[SNACKBARS] store snackbar', props<{s: Snackbar}>())
export const clearSnackbar = createAction('[SNACKBARS] clear snackbar')
