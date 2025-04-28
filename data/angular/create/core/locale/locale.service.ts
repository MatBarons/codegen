import { Injectable } from '@angular/core'
import { LocalStorageService } from 'ngx-webstorage'
import { Localstorage } from '../../../enums/localstorage'
import { distinctUntilChanged } from 'rxjs'
import { TranslocoService } from '@ngneat/transloco'

@Injectable({
  providedIn: 'root'
})
export class LocaleService {

  constructor (
    private readonly localStorage: LocalStorageService,
    private readonly translocoService: TranslocoService,
  ) { }

  getLocale (): string {
    this.localStorage.observe(Localstorage.LOCALE).pipe(
      distinctUntilChanged()
    ).subscribe(() => {
      location.reload()
    })
    const l = this.localStorage.retrieve(Localstorage.LOCALE) ?? 'en'
    this.translocoService.setActiveLang(l)
    return l
  }

  setLocale (l: string): void {
    this.localStorage.store(Localstorage.LOCALE, l)
  }
}
