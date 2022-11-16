import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent implements OnInit {
  @Output() submitted = new EventEmitter<string>();
  term = ''

  constructor() { }

  ngOnInit(): void {
  }

  // onInput(e: EventTarget) {
  //   this.term = (<HTMLInputElement>e).value;
  // }
  onFormSubmit(e: any) {
    e.preventDefault()
    this.submitted.emit(this.term)
  }



}
