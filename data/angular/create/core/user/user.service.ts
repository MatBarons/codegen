import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Store } from '@ngrx/store';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor(
    private readonly http: HttpClient,
    private readonly store: Store<AppState>
  ) {}
}
