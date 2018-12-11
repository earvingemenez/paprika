import * as _ from 'lodash';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';


export class Form1 {
  form: FormGroup;

  constructor (private baseform: Object) {
    // initialize form builder
    this.form = new FormBuilder().group(this.construct());
  }

  /* construct the form with the appropriate fields
   * and validations.
   */
  construct () {
    return _.mapValues(this.fieldset(), (v, k) => { return [null, v]; });
  }

  /* FIELDSET
   * list of form fields in dictionary form.
   * FIELD_NAME as key, VALIDATIONS as value
   */
  fieldset () {
    return Object.keys(this.baseform)
      .reduce((f, k) => { f[k] = this.baseform[k]; return f; }, {});
  }

  /* DEFAULT VALUE
   * set the value of the form fields if there is a default value.
   */
  defaultValue (d) {
    // set a timeout just incase that the value is not yet ready.
    setTimeout(() => { this.form.patchValue(d); }, 30);
  }
}


export class Form {
  constructor (public form: FormGroup) {}

  /* Check if the form field is valid
   */
  valid (f) {
    return !(!this.form.get(f).valid && this.form.get(f).touched);
  }

  /* Check if the form field has an error
   */
  hasError(f, e) {
    return this.form.get(f).hasError(e) && this.form.get(f).touched;
  }

}