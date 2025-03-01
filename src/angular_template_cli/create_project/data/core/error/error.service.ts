import { Injectable } from '@angular/core'
import { ErrorComponent } from './error/error.component'
import { Subscription } from 'rxjs'
import { MatDialog, MatDialogRef } from '@angular/material/dialog'

@Injectable({
  providedIn: 'root'
})
export class ErrorService {
  private errorModal?: MatDialogRef<ErrorComponent>
  private isOpen: boolean = false

  constructor (
    private readonly dialogService: MatDialog
  ) {}

  openErrorDialog (title: string | number, text: string): void {
    if (!this.isOpen) {
      this.errorModal = this.dialogService.open(
        ErrorComponent,
        {
          data: {
            title, text
          },
        })
      this.isOpen = true
      const s: Subscription | undefined = this.errorModal.afterClosed()?.subscribe(() => {
        this.isOpen = false
        s?.unsubscribe()
      })
    }
  }
}
