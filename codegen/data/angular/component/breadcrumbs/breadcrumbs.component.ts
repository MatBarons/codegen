import {Component} from '@angular/core';
import {Store} from "@ngrx/store";
import {AppState} from "../../app-state/app-reducers/app.reducers";
import {selectBreadcrumb} from "./breadcrumb.selectors";
import {toSignal} from "@angular/core/rxjs-interop";
@Component({
  selector: 'breadcrumbs',
  templateUrl: './breadcrumbs.component.html',
  styleUrl: './breadcrumbs.component.scss'
})
export class BreadcrumbsComponent{
  breadcrumbs = toSignal(this.store.select(selectBreadcrumb),{initialValue: []});
  constructor(private store : Store<AppState>) {}
}
