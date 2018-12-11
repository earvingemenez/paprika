/* Model class for user
 */
export class User {
  id : string = null;
  email : string = null;
  first_name : string = null;
  last_name : string = null;
  display_name : string = null;
  title : string = null;
  bio : string = null;
  handle : string = null;
  image : string = null;
  cover : string = null;
  subscribers : number[] = [];

  constructor(data={}) {
    Object.assign(this, data);
  }
}