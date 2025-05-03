constructor(
    private store: Store<AppState>,
    private destroyRef: DestroyRef,
    private component_nameService: component_nameService,
    private route: ActivatedRoute,
)

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
        ArtworkActions.storecomponent_nameFilters({ s: this.filterForm.value })
    );
}