package com.animals.animals;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

import java.util.List;

@EnableMongoRepositories
public interface AnimalRepository extends MongoRepository<Animals, String> {

//    @Query("{ 'name' : ?0 }")
    public Animals getAnimalsByName(String name);
}
