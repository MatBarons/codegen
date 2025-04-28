import { ChangeDetectionStrategy, Component, Inject } from '@angular/core'
import {MAT_DIALOG_DATA} from '@angular/material/dialog'
@Component({
  selector: 'error',
  templateUrl: './error.component.html',
  styleUrls: ['./error.component.scss'],
  standalone: false,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ErrorComponent {
  constructor(
    @Inject(MAT_DIALOG_DATA) public readonly data: {title: string, text: string}
  ) {}
}
