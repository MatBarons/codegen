import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor, HttpErrorResponse } from '@angular/common/http'
import { catchError, finalize, Observable, throwError } from 'rxjs'
import { Store } from '@ngrx/store'
import { LoaderActions } from './loader-state/actions'

@Injectable()
export class LoaderInterceptor implements HttpInterceptor {

  constructor(
    private readonly store: Store
  ) {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    if(!request.headers.has('Loader')){
      this.store.dispatch(LoaderActions.openLoader())
      return next.handle(request).pipe(
        catchError((error: HttpErrorResponse) => {
          return throwError(error)
        }),
        finalize(()=> {
          this.store.dispatch(LoaderActions.closeLoader())
        })
      )
    }else{
      const newReq = request.clone({
        headers: request.headers.delete('Loader','no-loader')
      })
      return next.handle(newReq).pipe(
        catchError((error: HttpErrorResponse) => {
          return throwError(error)
        })
      )
    }

  }
}
