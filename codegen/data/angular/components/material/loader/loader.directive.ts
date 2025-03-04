import { Directive, OnInit, TemplateRef, ViewContainerRef } from '@angular/core'
import { Store } from '@ngrx/store'
import { AppState } from '../../app-state/app-reducers/app.reducers'
import { LoaderSelectors } from './loader-state/selectors'

@Directive({
  selector: '[loader]'
})
export class LoaderDirective implements OnInit {
  private isVisible: boolean = false

  constructor (
    public readonly store: Store<AppState>,
    private readonly templateRef: TemplateRef<LoaderDirective>,
    private readonly viewContainerRef: ViewContainerRef
  ) { }

  ngOnInit (): void {
    this.store.select(LoaderSelectors.selectLoadersState).subscribe((l) => {
      if (l && !this.isVisible) {
        this.viewContainerRef.createEmbeddedView(this.templateRef)
        this.isVisible = true
      }
      if (!l) {
        this.viewContainerRef.clear()
        this.isVisible = false
      }
    })
  }

}
