import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
import { SnackbarsEffects } from './core/snackbars/snackbars-state/effects';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }), 
    provideRouter(routes),
    provideStore(),
    provideEffects(SnackbarsEffects.SnackbarsEffects)
    provideState({ name: 'project_name', reducer: appReducer }),
    provideNgxWebstorage(
        withNgxWebstorageConfig({ separator: ':', caseSensitive: true }),
        withLocalStorage(),
        withSessionStorage()
    ),
    provideHttpClient([ErrorInterceptor,LoaderInterceptor])
  ]
};