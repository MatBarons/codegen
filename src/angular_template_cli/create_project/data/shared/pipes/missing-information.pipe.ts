import { Pipe, PipeTransform } from '@angular/core'; 
import {TranslocoService} from "@ngneat/transloco";

@Pipe({
  name: 'missingInformation',
  standalone: true
})
export class MissingInformationPipe implements PipeTransform {

  constructor(private readonly translocoService: TranslocoService) {}
  transform(value: string|null|undefined): string {
    return value ?? this.translocoService.translate('missingInformation')
  }
}
