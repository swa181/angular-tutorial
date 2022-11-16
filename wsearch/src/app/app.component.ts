import { Component } from '@angular/core';
import { WikipediaService, WikipediaResponse } from './wikipedia.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  pages:{
    pageid: number;
    title: string;
    snippet: string;
  }[] = [];

  constructor(private wikipedia: WikipediaService) {

  }

  title = 'wsearch';

  onTerm(term: string) {
    this.wikipedia.search(term).subscribe((response) => {
      this.pages = response
    })
  }
}
