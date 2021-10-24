import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
@Component({
  selector: 'app-lat-lng',
  templateUrl: './lat-lng.component.html',
  styleUrls: ['./lat-lng.component.css']
})
export class LatLngComponent implements OnInit {
  
  title = 'Latitude and Longitude';
  checkoutForm = this.formBuilder.group({
    lat :'',
    lng :''
  });
  

  constructor(
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
  }


  onSubmit(): void{
    console.log(this.checkoutForm.value);
  }

}
