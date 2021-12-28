// contracts/OurToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Jemini is ERC20 {
    // In Wei
    constructor(uint256 initialSupply) ERC20("Jemini", "JEM") {
        _mint(msg.sender, initialSupply);
    }
}
