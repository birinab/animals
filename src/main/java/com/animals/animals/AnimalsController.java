package com.animals.animals;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class AnimalsController {

    @Autowired
    AnimalRepository animalRepository;

    @PostMapping("/getAnimal")
    public Animals getAnimal(@RequestBody String name) {
        return animalRepository.getAnimalsByName(name);
    }
}
