import { Injectable } from '@angular/core'
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor, HttpErrorResponse } from '@angular/common/http'
import { catchError, Observable, throwError } from 'rxjs'
import { ErrorService } from './error.service'

@Injectable()
export class ErrorInterceptor implements HttpInterceptor {

  constructor (
    private readonly errorService: ErrorService
  ) {}

  intercept (request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    return next.handle(request).pipe(
      catchError((e: HttpErrorResponse) => {
        this.errorService.openErrorDialog(e.status.toString(), e.error.message)
        return throwError(e)
      })
    )
  }
}
