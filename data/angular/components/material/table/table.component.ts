import { Component, DestroyRef, OnInit } from '@angular/core';
import { component_nameService } from '../component_name.service';
import { FormControl, FormGroup } from '@angular/forms';
import { Store } from '@ngrx/store';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { component_nameSelectors } from './component_name-state/selectors';
import { component_nameActions } from './component_name-state/actions';
import {component_name} from '../models/component_name';
import {component_nameFilters,component_nameFiltersForm } from '../models/component_name-filters.model';
import { distinctUntilChanged, Observable } from 'rxjs';
import { AppState } from '../../../app-state/app-reducers/app.reducers';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'project_name-component_name-table',
  templateUrl: './component_name-table.component.html',
  styleUrl: './component_name-table.component.scss'
})
export class ArtworksTableComponent implements OnInit{
  artworks: Array<component_name> = [];

  constructor(
    private component_nameService: component_nameService,
    private route: ActivatedRoute,
  ) {}

  

  get_component_name() {
    this.component_nameService
      .getcomponent_name(this.filterForm.value)
      .subscribe((r: component_name) => {
        this.component_name = r;
      });
  }

  goDetail (code: string): void {
    this.router.navigate([code], { relativeTo: this.route })
  }
}
