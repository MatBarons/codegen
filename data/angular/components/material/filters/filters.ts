import { AppState } from '../../../app-state/app-reducers/app.reducers';
import { Store } from '@ngrx/store';
import { FormControl, FormGroup } from '@angular/forms';
import { distinctUntilChanged, Observable } from 'rxjs';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { component_nameSelectors } from './component_name-state/selectors';
import { component_nameActions } from './component_name-state/actions';

filters$: Observable<component_nameFilters> = this.store.select(
    component_nameSelectors.selectcomponent_nameFilters
  );
filterForm: FormGroup<component_nameFiltersForm> = new FormGroup<component_nameFiltersForm>(
    {
        title: new FormControl(''),
        maker: new FormControl(''),
        creationDate: new FormControl(''),
        collections: new FormControl([]),
        loan: new FormControl(),
    }
);

constructor(
    private store: Store<AppState>,
    private destroyRef: DestroyRef,
    private component_nameService: component_nameService,
    private route: ActivatedRoute,
)



ngOnInit() {
    this.observePageState();
}

observePageState() {
    this.filters$.pipe(distinctUntilChanged(), takeUntilDestroyed(this.destroyRef)).subscribe((filters) => {
        this.component_name = [];
        this.filterForm.patchValue(filters);
        this.getcomponent_name();
    });
}

setFilter() {
    this.store.dispatch(
        component_nameActions.storecomponent_nameFilters({ s: this.filterForm.value })
    );
}