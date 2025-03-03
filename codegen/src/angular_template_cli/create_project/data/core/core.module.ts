import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslocoDirective } from '@ngneat/transloco';
import { LoaderComponent } from './loader/loader/loader.component';
import { LoaderDirective } from './loader/loader.directive';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { EffectsModule } from '@ngrx/effects';
import { SnackbarsEffects } from './snackbars/snackbars-state/effects';

@NgModule({
  declarations: [
    LoaderComponent,
    LoaderDirective
  ],
  exports: [
    LoaderComponent,
    LoaderDirective,
  ],
  imports: [
    CommonModule,
    TranslocoDirective,
    ReactiveFormsModule,
    FormsModule,
    RouterLink,
    RouterLinkActive,
    EffectsModule.forFeature([SnackbarsEffects.SnackbarsEffects])
  ],
})
export class CoreModule {}
