import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-views-home',
  templateUrl: './views-home.component.html',
  styleUrls: ['./views-home.component.css'],
})
export class ViewsHomeComponent implements OnInit {
  stats = [
    { value: 22, label: '# of Users' },
    { value: 900, label: 'Revenue' },
    { value: 50, label: 'Reviewss' },
  ];

  items = [
    {
      image: '/assets/images/couch.jpeg',
      title: 'couch',
      description: 'this is noice',
    },
    {
      image: '/assets/images/dresser.jpeg',
      title: 'Dresser',
      description: 'this is gud',
    },
  ];

  constructor() {}

  ngOnInit(): void {}
}
