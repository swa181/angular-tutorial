import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  name: string = "";
  date: string ="";
  amount: number = 0;
  height: number = 0;
  miles: number = 0;

  car ={
    make:'Toyota',
    model: 'Camry',
    year: 2000
  }

  onMilesChange(event: EventTarget) {
    const target = event as HTMLInputElement;
    this.miles = parseFloat(target.value);
  }

  onHeightChange(event: EventTarget) {
    const target = event as HTMLInputElement;
    this.height = parseInt(target.value);
  }

  onNameChange(event: EventTarget) {
    const target = event as HTMLInputElement;
    this.name = target.value;
  }

  onDateChange(event: EventTarget) {
    const target = event as HTMLInputElement;
    this.date = target.value;
  }

  onAmountChange(event: EventTarget) {
    const target = event as HTMLInputElement;
    this.amount = parseFloat(target.value);
  }

}
