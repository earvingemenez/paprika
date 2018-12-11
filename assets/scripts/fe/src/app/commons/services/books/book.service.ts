import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { READS, RELEASES } from '../../constants/api.constants';


@Injectable({
  providedIn: 'root'
})
export class BookService {

  constructor(
    private http: HttpClient
  ) { }

  /* BOOK READ LOGS
   * @desc : get the read logs of the logged in user
   */
  reads () {
    return this.http.get(READS);
  }

  /* NEW RELEASES
   * @desc : get the list of new released books.
   *         books that are published 7 days ago or later
   */
  releases () {
    return this.http.get(RELEASES);
  }
}
