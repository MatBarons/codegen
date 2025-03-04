import { Injectable } from '@angular/core'
import { Actions, createEffect, ofType } from '@ngrx/effects'
import { SnackbarsActions } from '../actions'
import { tap } from 'rxjs'
import { MatSnackBar } from '@angular/material/snack-bar'
import { TranslocoService } from '@ngneat/transloco'

@Injectable()
export class SnackbarsEffects {
  openSnackbar$ = createEffect(() => {
    return this.actions$.pipe(
      ofType(SnackbarsActions.storeSnackbar),
      tap((s) => {
        this.snackbarService.open(
          this.translocoService.translate(s.s.text),
          this.translocoService.translate('button.close'),
          { duration: s.s.expiration }
        )
      })
    )
  }, { dispatch: false })

  constructor (
    private readonly actions$: Actions,
    private readonly snackbarService: MatSnackBar,
    private readonly translocoService: TranslocoService,
  ) {}
}
