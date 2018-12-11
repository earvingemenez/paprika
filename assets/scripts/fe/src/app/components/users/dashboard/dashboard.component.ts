import { Component, OnInit } from '@angular/core';

import { BookService } from '../../../commons/services/books/book.service';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  recent : any;
  releases : any;

  constructor(
    private books: BookService
  ) { }

  ngOnInit() {
    this.getRecentReads();
    this.getNewReleases();
  }

  getRecentReads () {
    this.books.reads()
      .subscribe(resp => { this.recent = resp; })
    ;
  }

  getNewReleases () {
    this.books.releases()
      .subscribe(resp => { this.releases = resp; })
  }
}