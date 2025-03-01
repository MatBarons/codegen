import {FormControl} from "@angular/forms";

export type AsFormControl<T> = {
  [K in keyof T]: FormControl<T[K] | null>;
};
